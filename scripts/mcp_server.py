"""Servidor MCP que expõe skills/especialista-dados/ para o Open Arena.

Substitui o fluxo antigo (`build-open-arena.ps1` gera `dist/open-arena/`, usuário sobe a pasta na
chain): agora o Open Arena aponta direto para este repositório no GitHub e o servidor da chain faz
`git pull` periódico. Este processo só precisa ficar de pé (transporte stdio) e servir o conteúdo
atual do disco — sem build, sem cache (cada leitura reabre o arquivo).

Escopo (só resources, nenhuma tool — decisão do usuário):
- `skills/especialista-dados/SKILL.md`;
- todo `skills/especialista-dados/references/**/*.md`, respeitando a exclusão de
  `config/fora-do-open-arena.txt` (mesma lista usada pelo `build-open-arena.ps1`);
- `skills/especialista-dados/assets/tema-oficial-powerbi.json` (único asset em texto/JSON na raiz de
  assets — fonts/logos/fotos binários continuam fora, não viram resource).

Segurança:
- nenhum acesso a `.env`, banco ou caminho fora da árvore de `skills/especialista-dados/`;
- cada leitura passa pela mesma máscara de segredo (`PADRAO_SEGREDO`) usada em `ler_conversas.py`,
  como defesa em profundidade — mesmo que o conteúdo de `references/` já devesse estar mascarado na
  origem.

Uso: registrado em `.mcp.json` (`python scripts/mcp_server.py`, transporte stdio).
"""

from __future__ import annotations

import re
from pathlib import Path

from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.resources import FunctionResource

RAIZ = Path(__file__).resolve().parent.parent
SKILL_DIR = RAIZ / "skills" / "especialista-dados"
SKILL_MD = SKILL_DIR / "SKILL.md"
REFERENCES_DIR = SKILL_DIR / "references"
TEMA_JSON = SKILL_DIR / "assets" / "tema-oficial-powerbi.json"
EXCLUSOES_TXT = RAIZ / "config" / "fora-do-open-arena.txt"

URI_ESQUEMA = "skill://"

PADRAO_SEGREDO = re.compile(
    r"(password\s*=\s*\S+|senha\s*=\s*\S+|pwd\s*=\s*\S+|uid\s*=\s*\S+|"
    r"connection[_ -]?string\s*[:=]\s*\S+|jdbc:\S+|server\s*=\s*\S+|"
    r"https?://[^\s]*(blob|token=)\S*|(api[_-]?key|token|secret)\s*[:=]\s*\S+)",
    re.IGNORECASE,
)


def mascarar(texto: str) -> str:
    return PADRAO_SEGREDO.sub("***", texto)


def _nomes_excluidos() -> set[str]:
    if not EXCLUSOES_TXT.exists():
        return set()
    linhas = EXCLUSOES_TXT.read_text(encoding="utf-8").splitlines()
    return {
        linha.strip()
        for linha in linhas
        if linha.strip() and not linha.strip().startswith("#")
    }


def _nome_achatado(caminho_relativo_a_references: Path) -> str:
    partes = caminho_relativo_a_references.parts
    if len(partes) > 1:
        return f"{partes[0]}-{partes[-1]}"
    return partes[0]


def _ler_mascarado(caminho: Path) -> str:
    return mascarar(caminho.read_text(encoding="utf-8"))


def _arquivos_disponiveis() -> dict[str, Path]:
    """Mapa {uri: caminho absoluto} de tudo que o servidor expõe, lido do disco a cada chamada."""
    excluidos = _nomes_excluidos()
    disponiveis: dict[str, Path] = {}

    if SKILL_MD.exists():
        disponiveis[f"{URI_ESQUEMA}SKILL.md"] = SKILL_MD

    if REFERENCES_DIR.exists():
        for caminho in sorted(REFERENCES_DIR.rglob("*.md")):
            rel = caminho.relative_to(REFERENCES_DIR)
            if _nome_achatado(rel) in excluidos:
                continue
            uri = f"{URI_ESQUEMA}references/{rel.as_posix()}"
            disponiveis[uri] = caminho

    if TEMA_JSON.exists():
        disponiveis[f"{URI_ESQUEMA}assets/tema-oficial-powerbi.json"] = TEMA_JSON

    return disponiveis


def criar_servidor() -> MCPServer:
    server = MCPServer("especialista-dados")
    for uri, caminho in _arquivos_disponiveis().items():
        mime = "application/json" if caminho.suffix == ".json" else "text/markdown"
        server.add_resource(
            FunctionResource(
                uri=uri,
                name=caminho.name,
                description=f"skills/especialista-dados/{caminho.relative_to(SKILL_DIR).as_posix()}",
                mime_type=mime,
                fn=lambda caminho=caminho: _ler_mascarado(caminho),
            )
        )
    return server


server = criar_servidor()


if __name__ == "__main__":
    import asyncio

    asyncio.run(server.run_stdio_async())
