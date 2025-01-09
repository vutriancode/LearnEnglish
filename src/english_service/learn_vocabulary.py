import google.generativeai as genai
import random
# from src.notification_service.reply import *
from src.google_sheet.utils import get_vocabulary_for_today
def vocabulary_for_today():
    vocabulary = get_vocabulary_for_today()
    keyword = random.choice(vocabulary.values.tolist())[0]
    genai.configure(api_key="AIzaSyCqHprbJMRlaLGGYFSFJ7au04mbpDq2KSA")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("""
    Imagine you are an English teacher and you are guiding your students to learn vocabulary by sending a message for them . For example, “beautify” word will have message:
    <b>beautify /ˈbjuː.t̬ə.faɪ/</b> 
    <b>Meaning:</b> 
    <b>English:</b> To make something more beautiful.
    <b>Vietnamese:</b> Làm đẹp, tô điểm.
                                      
    <b>Grammatical forms:</b> 
    <b>Noun: beauty /ˈbjuː.t̬i/</b>
    <i>example: The sunset was a breathtaking display of natural beauty (Hoàng hôn là một màn trình diễn ngoạn mục của vẻ đẹp tự nhiên.)</i>
                                      
    <b>Verb: beautify /ˈbjuː.t̬ə.faɪ/</b> 
    <i>example: The city council plans to beautify the park with new flowers and benches (Hội đồng thành phố có kế hoạch làm đẹp công viên bằng hoa và ghế dài mới)</i>
    
    <b>Adjective: beautiful /ˈbjuː.t̬ə.fəl/</b> 
    <i>example: "You have the most beautiful smile (Bạn có nụ cười đẹp nhất)"</i> 
    
    <b> Adverb: beautifully /ˈbjuː.t̬ə.fəl.i/</b> 
    <i>example: "The garden was beautifully landscaped with colorful flowers (Khu vườn được tạo cảnh đẹp với những bông hoa đầy màu sắc)"</i> 
    """
    +f"Now, you return message for '{keyword}' word, you must keep response same format html above.""")
    return response.text