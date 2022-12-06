package main 

import (
  "fmt"
  "io/ioutil"
  "net/http"
  "os"
  "strings"
)


var BASE_URL = "https://raw.githubusercontent.com/"


func main() {

  if len(os.Args) == 1 {
    fmt.Println("Supply a url plz")
  }

  url := os.Args[1]
  split_url := strings.Split(url, "/")

  if len(split_url) <= 1 {
    fmt.Println("Couldn't split url by '/' character") 
    os.Exit(1)
  }

  file_name := split_url[len(split_url)-1]

  url = strings.Replace(url, "/blob", "", 1)
  github := "github.com/" 
  github_len := len(github)
  index := strings.Index(url, github)

  url = BASE_URL + url[index + github_len:]

  // get data from url
  response, err := http.Get(url)

  if err != nil {
    fmt.Fprintf(os.Stderr, "Fetch: %v\n", err)
    os.Exit(1)
  }

  // extract data
  text, err := ioutil.ReadAll(response.Body)
  response.Body.Close()

  if err != nil {
    fmt.Fprintf(os.Stderr, "Fetch: reading %s %v\n", url, err)
  }

  // write to file
  err = os.WriteFile("./" + file_name, text, 0644)
  if err != nil {
    fmt.Fprintf(os.Stderr, "Fetch: writing %v\n", err)
  }
}
  


