def resume_result_wrapper(resume):
    parser = ResumeParser(resume)
    return parser.get_extracted_data()
