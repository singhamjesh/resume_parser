import os
import json
from src.validator.agent import AgentSchema
from src.config.logger import Logger
from src.resume_parser.index import ResumeParser
import multiprocessing as mp
import src.utils.helper as resume_result_wrapper


class ExecutionController:
    """
    This class represents the controller for executing a task.
    """

    def __init__(self):
        self.logger = Logger()

    # def resume_result_wrapper(resume, x):
    #     base_dir = os.path.abspath(os.path.join(os.getcwd()))
    #     resume_path = os.path.join(base_dir, resume)
    #     print(resume_path)
    #     parser = ResumeParser(resume_path)
    #     return parser.get_extracted_data()

    def execute(self, payload: AgentSchema) -> dict:
        try:
            self.logger.info('ExecutionController.parse() method called')

            # Get payload data
            payload = payload.dict()

            base_dir = os.path.abspath(os.path.join(os.getcwd()))
            resume = os.path.join(base_dir, 'resumes/amjesh_cv.pdf')

            print(resume)
            parser = ResumeParser(resume)
            result = parser.get_extracted_data()
            print(result)

            # pool = mp.Pool(mp.cpu_count())
            # resumes = []
            # data = []
            # for root, directories, filenames in os.walk('resumes'):
            #     for filename in filenames:
            #         file = os.path.join(root, filename)
            #         resumes.append(file)

            # print(resumes)
            # results = [pool.apply_async(
            #     self.resume_result_wrapper, args=(x,)) for x in resumes]

            # results = [p.get() for p in results]

            self.logger.info('Function execute: Execution complete')
            return {"result": result}
        except Exception as e:
            self.logger.error(
                'Getting Error in ExecutionController.execute:', e)
            raise e
