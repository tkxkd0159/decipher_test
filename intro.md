# Basic Algorithm Test
해당 링크에 접속하신 후 주어진 조건에 맞추어 문제를 해결해주세요.
## Problem 1
[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
## Problem 2
[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
# Query Test
클라이언트 프로그램을 통해 블록체인 메인넷 정보를 받아오거나 다른 노드와 상호작용을 하기 위해서는 쿼리하는 것이 필요합니다.  
따라서 해당 test는 조건에 맞게 간단한 REST API 및 JSON-RPC 요청을 날릴 수 있는지에 대한 검증을 진행합니다.

1) ~ 로 POST 요청  
아래 양식의 JSON 형태로 해당 엔드포인트로 POST 요청을 보내주시고 리턴되는 시드 값을 저장해주세요.  
이 때 이름, 나이를 본인의 정보에 맞게 채워넣어 주세요.
```json
{
    name: "SatoshiNakamoto",
    age: 20
}
```
2) ~로 JSON-RPC Request 보내기  
1\)에서 얻은 `seed` 값을 `name`, `age`값과 함께 채워넣고 아래 양식으로 해당 엔드포인트로 JSON-RPC request를 보내주세요. 이 때 성공메세지와 함께 특정 숫자가 반환되면 이를 지원서에 적어주시면 됩니다.
```json
{
    "jsonrpc": "2.0",
    "method": "genUniqueID",
    "params": {"name": "SatoshiNakamoto", "age": 20, "seed": "<hex_str>"},
    "id": 202108
}
```
Example response
```
{"id":202108,"jsonrpc":"2.0","result":"Success!!! Your ID is : 116980bd32321260_1628661963"}
```