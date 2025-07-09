# 📝 DOCX Placeholder Filler (with Image and Embedded Excel Support)

## Description

This Python tool automatically replaces **placeholders** in Microsoft Word `.docx` documents with **text**, **images**, or **data from embedded Excel files**. It's ideal for generating templates like **contracts**, **certificates**, **reports**, and **dynamic documents**.

---

## ✨ Features

* 🔤 Replace **text placeholders** in `.docx` files
* 🖼️ Insert **images** into Word using placeholders
* 📊 Modify **embedded Excel files** (`.xlsx`) that used to generate plot, chart or anything else inside Word documents
* 🧩 **Supports placeholders inside textboxes**
* 🧾 Detect **unfilled placeholders**
* ✅ **Preserve existing comments** in .docx documents
* 🧠 Smart parsing of complex or multiline placeholder structures



---

## 📦 Installation

```bash
pip install docxfill
```

---

## 🧱 Placeholder Format

| Type   | Syntax Example                | Replacement Type |
| ------ | ----------------------------- | ---------------- |
| Text   | `{{name}}`                    | String           |
| Number | `{{age}}`                     | Int / Float      |
| Image  | `{{profile_picture}}`         | Image path       |
| Excel  | `{{invoice_total}}` (in cell) | Cell content     |

---

## 🚀 Usage

### 1. Run `execute()`

```python
from docxfill.fill import execute

result = execute(
    file_path="template.docx",             # Input .docx file
    output_file_path="output.docx",        # Output .docx file
    text_content={"name": "John", "age": "30"},
    image_content={"profile_picture": "images/photo.jpg"},
    state_dir="./test_files"               # Optional working directory
)

print(result)
```

### 2. Sample Output

```json
{
  "tool": "docx_fill_with_image",
  "success": true,
  "output_file_path": "output.docx",
  "filled": {
    "name": "John",
    "age": "30",
    "profile_picture": "images/photo.jpg"
  },
  "unfilled_placeholder": ["email", "address"]
}
```

---

## 🔍 Key Functions

| Function                                         | Description                        |
| ------------------------------------------------ | ---------------------------------- |
| `replace_text_in_paragraph()`                    | Replace text in regular paragraphs |
| `replace_text_in_excel_sheet()`                  | Replace text inside Excel cells    |
| `extract_and_modify_embedded_excel()`            | Modify embedded `.xlsx` content    |
| `find_inner_placeholders_in_docx()`              | Find any unfilled placeholders     |
| `execute()`                                      | Main function to run all processes |
| ✅ Supports placeholder inside Word **textboxes** |                                    |

---

## 📁 Folder Structure Example

```
test_files/
├── template.docx
├── output.docx
└── images/
    └── photo.jpg
```

---

## ⚠️ Notes

* Only supports `.docx` (not `.doc`)
* Embedded Excel files must be `.xlsx` format
* Placeholders must follow the `{{placeholder}}` format
* Images must be valid paths (relative or absolute)

---

## 📄 License

MIT License — Free for personal and commercial use.
