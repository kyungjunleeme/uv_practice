from pypi_attestations.verify import verify
from pypi_attestations.models import Distribution, GitHubPublisher

dist = Distribution.from_artifact_and_provenance(
    artifact_path=Path("dist/my_package-0.1.0-py3-none-any.whl"),
    provenance_path=Path("provenance-0.1.0.intoto.jsonl"),
)

publisher = GitHubPublisher(
    owner="kyungjunleeme",
    repo="uv_practice",
    ref="refs/tags/0.1.0",
    workflow="publish.yml",
)

result, metadata = verify(
    identity=publisher,
    dist=dist,
    staging=False,
    offline=False,
)

print("Verification result:", result)
