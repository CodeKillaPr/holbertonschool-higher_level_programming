name: Docker Image Build and Push

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Build Docker image
        run: docker build -t <image-name> .

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v1
        with:
          registry: ghcr.io
          username: ${{ github.repository_owner }}
          password: ${{ secrets.CR_PAT }}

      - name: Push Docker image
        run: docker push ghcr.io/${{ github.repository_owner }}/<image-name>:${{ github.sha }}