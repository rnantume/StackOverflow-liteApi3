"""contains various routes for the questions endpoints"""

from flask import request, jsonify, Blueprint, abort
from flask_restful import (reqparse, Resource, fields, inputs, Api,
                            marshal)

from API.models.allmodels import Question


class AnswerList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('answer', type=str, required=True, 
                            nullable=False, help="answer cannot be null or none",
                            location = ['form', 'json']
                            )   
        self.reqparse.add_argument('accepted', choices=('True','False'),
                            default=False, store_missing=True, location = ['form', 'json']
                            )
        super().__init__()

    def get(self, questionId):
        """
        get all answers on a specific question by questionId
        """
        try:
            answers = Answer.get_question_answers(questionId)
        except TypeError:
            abort(404, "message = question {} doesnot exist".format(questionId))
        else:
            return {'answers': [marshal(answer, answer_fields)
                                for answer in answers]}, 200

    def post(self, questionId):
        """
        adding an answer to a specific question by questionId
        """
        try:
            answers = Answer.get_question_answers(questionId)
        except TypeError:
            abort(404, "message = question {} doesnot exist".format(questionId))
        else:
            args = self.reqparse.parse_args()
            new_answer = Answer(**args).add_answer(questionId)
            """
            serializing the response with JSON
            """
            return {'Your answer': [marshal(new_answer, answer_fields)]},201


class Answer_(Resource):
    pass



answers_bp = Blueprint('resources.answers', __name__)
ans_api = Api(answers_bp)

ans_api.add_resource(AnswerList,
    '/StackOverflow-lite/api/v1/questions/<int:questionId>/answers',
    endpoint='answers')

ans_api.add_resource(Answer_,
    '/StackOverflow-lite/api/v1/questions/<int:questionId>/answers/<int:answerId>',
    endpoint='answer')
