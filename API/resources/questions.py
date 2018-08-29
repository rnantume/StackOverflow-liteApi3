"""contains various routes for the questions endpoints"""

from flask import request, jsonify, Blueprint, abort
from flask_restful import (reqparse, Resource, fields, inputs, Api,
                            marshal)

from API.models.allmodels import Question


class QuestionList(Resource):
    """
    Shows a list of all questions
    """
        
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



questions_bp = Blueprint('routes', __name__)
qn_api = Api(questions_bp)

qn_api.add_resource(QuestionList,
    '/StackOverflow-lite/api/v1/questions',
    endpoint='questions')
