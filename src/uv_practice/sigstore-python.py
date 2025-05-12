from pathlib import Path
from sigstore._internal.verify import Verifier, VerificationMaterials
from sigstore.verify import Verifier
from sigstore import verify

# 경로 설정
bundle_path = Path("dist/uv_practice-0.8.0-py3-none-any.whl.intoto.jsonl")
artifact_path = Path("dist/uv_practice-0.8.0-py3-none-any.whl")

# 검증용 자료 로딩
materials = VerificationMaterials.from_paths(
    artifact_path=artifact_path,
    bundle_path=bundle_path,
)

# 검증 수행
verifier = Verifier.production()
result = verifier.verify(materials)

if result:
    print("✅ Sigstore verification PASSED (Statement v0.1)")
else:
    print("❌ Verification FAILED")
