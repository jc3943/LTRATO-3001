package main

import (
    b64 "encoding/base64"
    "fmt"
    "flag"
)

func main() {

    dataPtr := flag.String("d", "", "string to encode")
    flag.Parse()

    sEnc := b64.StdEncoding.EncodeToString([]byte(*dataPtr))
    fmt.Println(sEnc)

}