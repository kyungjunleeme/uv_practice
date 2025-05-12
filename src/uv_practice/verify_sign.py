from pathlib import Path
from pypi_attestations import Attestation, Distribution
from sigstore.verify import policy

# # 🔹 1. WHL 및 attestation 파일 경로 지정
# base_dir = Path(__file__).parent / "dist"
# print(base_dir)
#
# dist_path = base_dir / "uv_practice-0.6.0-py3-none-any.whl"
# attestation_path = base_dir / "provenance-0.6.0.intoto.jsonl"
#
# # 🔹 2. 배포 파일 및 attestation 로드
# dist = Distribution.from_file(dist_path)
# attestation = Attestation.model_validate_json(attestation_path.read_bytes())
#
# # 🔹 3. GitHub Actions OIDC 발급자 정보 기반 검증
# identity = policy.Identity(
#     identity="https://github.com/kyungjunleeme",  # 이메일 대신 GitHub URI 사용
#     issuer="https://token.actions.githubusercontent.com"
# )
#
# # 🔹 4. 검증 실행
# attestation.verify(identity=identity, dist=dist)
# print("✅ Attestation verification passed!")


# from pathlib import Path
# from sigstore.verify import verify
#
base_dir = Path(__file__).parent / "dist"
# print(base_dir)
#
dist_path = base_dir / "uv_practice-0.6.0-py3-none-any.whl"
bundle_path = base_dir / "provenance-0.6.0.intoto.jsonl"
#
# # 검증 실행
# result = verify(
#     artifact_path=dist_path,
#     bundle_path=bundle_path,
#     offline=False  # transparency log를 확인하려면 False
# )
#
# if result:
#     print("✅ Sigstore bundle verification passed!")
# else:
#     print("❌ Verification failed.")

from pathlib import Path
from pypi_attestations import Attestation, Distribution
from sigstore.models import Bundle
from sigstore.verify import policy

# # 📦 .whl 파일 경로
# dist_path = Path("dist/uv_practice-0.8.0-py3-none-any.whl")
#
# # 📄 .intoto.jsonl 파일 경로 (Sigstore bundle)
# bundle_path = Path("dist/uv_practice-0.8.0-py3-none-any.whl.intoto.jsonl")

# 1. Distribution 로드
dist = Distribution.from_file(dist_path)

# 2. Sigstore bundle -> Attestation 객체로 변환
with bundle_path.open("rb") as f:
    bundle = Bundle.from_json(f.read())
attestation = Attestation.from_bundle(bundle)

# 3. GitHub Actions 발급자 기반 정책 설정
# identity = policy.Identity(
#     identity="https://github.com/kyungjunleeme",  # 로그의 Subject URI
#     issuer="https://token.actions.githubusercontent.com"
# )

# 검증 정책: 실제 SAN 값 기준
identity = policy.Identity(
    identity="https://github.com/slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@refs/tags/v2.1.0",
    issuer="https://token.actions.githubusercontent.com"
)

# 4. 검증 실행
attestation.verify(identity=identity, dist=dist)
print("✅ Attestation verification passed!")
