from docxfill import fill

def test_fill():
    result = fill(
        file_path='tests/input.docx',
        output_file='tests/output.docx',
        text={"foo": "bar"}
    )
    assert result["success"] == True