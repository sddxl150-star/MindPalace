import re

# 读取文件
with open('skills.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 移除 toggle 按钮
content = content.replace(
    '<div class="translation-toggle"><span class="toggle-text">显示翻译</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 9l-7 7-7-7"/></svg></div>',
    ''
)

# 使用正则表达式将段落和翻译包裹在 translatable-section 中
# 匹配 <p>...</p> 后跟 <div class="translation">...</div>
pattern = r'(<p[^>]*>.*?</p>)\s*(<div class="translation">.*?</div>)'
replacement = r'<div class="translatable-section">\1\2</div>'
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 匹配 <h2>...</h2> 后跟 <div class="translation">...</div>
pattern = r'(<h2[^>]*>.*?</h2>)\s*(<div class="translation">.*?</div>)'
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 匹配 <h3>...</h3> 后跟 <div class="translation">...</div>
pattern = r'(<h3[^>]*>.*?</h3>)\s*(<div class="translation">.*?</div>)'
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 写入文件
with open('skills.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成！")
