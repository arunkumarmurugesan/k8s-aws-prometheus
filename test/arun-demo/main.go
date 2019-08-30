package main

import (
  "fmt"
)

func GetHello() string {
  return "Hello World!"
}

func main() {
  output := GetHello()
  fmt.Println(output)
}
