golangci-lint := require("golangci-lint")

[group("go")]
lint:
    golangci-lint run

fmt:
    go fmt -w . && \ 
    just --fmt --unstable
