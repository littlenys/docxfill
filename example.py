from docxfill.fill import fill

result = fill(
    file_path='input.docx',
    output_file='output.docx',
    text={"foo": "bar", "amount": 123},
    images={"photo": "/absolute/path/image.jpg"}
)

print("Success :", result["success"])
print("Filled :", result["filled"])
print("Unfilled :", result["unfilled"])