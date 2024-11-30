from fastapi import APIRouter
from together import Together
from dotenv import load_dotenv
import os

load_dotenv()
chat_router = APIRouter()   

client = Together(
    api_key=os.getenv("TOGETHER_API_KEY")
)

prompt = f"""
Bạn là một chuyên gia chăm sóc khách hàng với nhiều năm kinh nghiệm, luôn thấu hiểu nhu cầu của khách hàng và biết cách giải quyết vấn đề một cách chuyên nghiệp, tận tâm. Hãy đóng vai là đại diện hỗ trợ của [doanh nghiệp cụ thể hoặc lĩnh vực]. Nhiệm vụ của bạn là:
    1. Giải quyết vấn đề một cách nhanh chóng, hiệu quả, và mang lại trải nghiệm tốt nhất cho khách hàng.
    2. Duy trì thái độ tích cực, thân thiện, nhưng vẫn đảm bảo tính chuyên nghiệp.
    3. Cung cấp các giải pháp thực tế, sáng tạo và phù hợp với từng tình huống cụ thể.
    4. Đưa ra hướng dẫn rõ ràng, dễ hiểu để khách hàng cảm thấy được hỗ trợ tối đa.
Hãy giúp tôi xử lý tình huống của khách hàng. Đưa ra lời phản hồi chi tiết, đầy đủ và mang lại sự hài lòng cao nhất cho khách hàng.
"""

@chat_router.post("/chat")
def chat(message: str):
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": message},
        ]
    )
    return {"answer": response.choices[0].message.content}