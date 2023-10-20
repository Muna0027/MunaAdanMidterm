from flask import Flask, jsonify, request
students = {
        '1': {'name': 'Muna', 'grade': 'A+'}
}

app = Flask(__name__)

@app.route('/student/<id>')
def students(id):

    student_info = students.get(id, {})
    print(student_info)
    return jsonify(student_info)

@app.route('/student', methods=['POST'])
def create_student():
    new_student = request.get_json()
    
    
    required_keys = ['name', 'grade']
    if all(key in new_student for key in required_keys):
        students[str(len( students.keys()) + 1)] = new_student
        print( students)
        return jsonify({"success":"Successed"})
    else:
        return jsonify({"success":False, "msg": "add all data "})
    
@app.route('/student/<id>', methods=['PUT'])
def update_student(id):
 
    if id in  students:
        updated_student = request.get_json()

        required_keys = ['name', 'grade']
        if all(key in updated_student for key in required_keys):
            students[id] = updated_student
            print( students)
            return jsonify({"success": True, "msg": "updated successfully"})
        else:
            return jsonify({"success": False, "msg": "Please pass all the required"}), 400
    else:
        return jsonify({"success": False, "msg": "not found"}), 404
    
@app.route('/student/<id>', methods=['DELETE'])
def delete_student(id):
    if id in  students:
       
        del  students[id]
        return jsonify({"success": True, "msg": "deleted successfully"})
    else:
        return jsonify({"success": False, "msg": "not found"}), 404





if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)