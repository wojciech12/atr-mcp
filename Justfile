golangci-lint := require("golangci-lint")

[group("go")]
lint:
    golangci-lint run

fmt:
    golangci-lint format
