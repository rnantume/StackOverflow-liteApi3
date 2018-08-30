"""contains various routes for the questions endpoints"""

from flask import request, jsonify, Blueprint, abort
from flask_restful import (reqparse, Resource, fields, inputs, Api,
                            marshal)

from API.models.allmodels import Question


class QuestionList(Resource):
    """
    Shows a list of all questions, and lets one POST to add new question
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('Topic', type=str, required=True, 
                            nullable=False, help="Topic cannot be null or none",
                            location = ['form', 'json']
                            )
        self.reqparse.add_argument('Description', type=str, required=True, 
                            nullable=False, help="Description cannot be null or none",
                            location = ['form', 'json']
                            )
        super().__init__()
        
    def get(self):
        """
        get all questions
        """
        questions = Question.get_questions()
        if questions:
            """serializing the response with JSON"""
            return {'Questions': questions},200
        else:
            return {'Message': 'No Questions Found'},200

    def post(self):
        """
        create a new question
        """
        args = self.reqparse.parse_args()
        new_question = Question(**args).add_question()
        """serializing the response with JSON"""
        return {'Your Question':[marshal(new_question, question_fields)]},201

class Question_(Resource):
    def get(self, questionId):
        """
        get a specific question
        """
        question = Question.get_question(questionId)
        if question:
            return {'Your question': [marshal(question,question_fields)]}, 200
        else:
            abort(404, "question {} doesnot exist".format(questionId))


questions_bp = Blueprint('resources.questions', __name__)
qn_api = Api(questions_bp)

qn_api.add_resource(QuestionList,
    '/StackOverflow-lite/api/v1/questions',
    endpoint='questions')

qn_api.add_resource(Question_,
    '/StackOverflow-lite/api/v1/questions/<int:questionId>',
    endpoint='question')