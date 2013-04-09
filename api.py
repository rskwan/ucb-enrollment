from flask import Flask, render_template, url_for
from flask.ext.restful import abort, Api, Resource
from dbaccess import get_course_map, get_enroll_info

app = Flask(__name__)
api = Api(app)

@app.route('/')
def welcome():
    return render_template('index.html')

class EnrollInfo(Resource):
    def get(self, ccn):
        info = get_enroll_info(ccn)
        if info:
            return info
        else:
            abort(404, message='CCN {} not found'.format(ccn))

class CourseMap(Resource):
    courses = {}
    def get(self):
        if len(self.courses.keys()) == 0:
            self.courses = get_course_map()
        return self.courses

class PhaseDates(Resource):
    phase_dates = { 'phase1': { 'start': '2013-04-08',
                                'end': '2013-07-07' },
                    'phase2': { 'start': '2013-07-09',
                                'end': '2013-08-17' },
                    'adjust': { 'start': '2013-08-18',
                                'end': '2013-09-27' } }
    def get(self):
        return self.phase_dates

api.add_resource(EnrollInfo, '/<string:ccn>')
api.add_resource(CourseMap, '/courses')
api.add_resource(PhaseDates, '/phases')

if __name__ == '__main__':
    app.run(debug=True)
