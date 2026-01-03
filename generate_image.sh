curl -X POST https://image-api.hiep622032001.workers.dev \
  -H "Authorization: Bearer 12345678" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "A cute appler cooking breakfast"}' \
  --output image.jpg