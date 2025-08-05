golangci-lint := require("golangci-lint")

[group("go")]
lint:
    golangci-lint run

fmt:
    golangci-lint fmt

prettier:
    npx prettier --write .
