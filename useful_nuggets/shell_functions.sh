build() {
  echo "example function"
  deploy
}
test() {
  echo "testing"
}

deploy() {
  test
  echo "deploying after successfully testing"
}
build
