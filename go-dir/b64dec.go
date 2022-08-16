package main

import (
    b64 "encoding/base64"
    "fmt"
    "flag"
)

func main() {

    dataPtr := flag.String("d", "", "string to decode")
    flag.Parse()

    sDec, _ := b64.StdEncoding.DecodeString(*dataPtr)
    fmt.Println(string(sDec))

}