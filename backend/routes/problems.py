from flask import Blueprint, request, jsonify
from backend.db import create_connection

problem_blueprint = Blueprint("problems", __name__, url_prefix="/problems")

# Get all problems
@problem_blueprint.route("/", methods=["GET"])
def get_all_problems():
    # get database connections and problems
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM problems")
    rows = cur.fetchall()
    conn.close()

    problems = []
    for row in rows:
        problems.append({
            "id": row[0],
            "title": row[1],
            "difficulty": row[2],
            "topic": row[3],
            "status": row[4],
            "notes": row[5],
            "date_added": row[6],
            "last_attempt": row[7]
        })
    return jsonify(problems)

# Get a specific problem by id
@problem_blueprint.route("/<int:problem_id>", methods=["GET"])
def get_problem(problem_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM problems WHERE id = ?", (problem_id,))
    row = cur.fetchone()
    conn.close()

    if row:
        problem = {
            "id": row[0],
            "title": row[1],
            "difficulty": row[2],
            "topic": row[3],
            "status": row[4],
            "notes": row[5],
            "date_added": row[6],
            "last_attempt": row[7]
        }
    return jsonify(problem)

# Add a new problem
@problem_blueprint.route("/", methods=["POST"])
def add_problem():
    data = request.get_json()
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO problems (title, difficulty, topic, status, notes)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data.get("title"),
        data.get("difficulty"),
        data.get("topic"),
        data.get("status"),
        data.get("notes", "")
    ))
    conn.commit()
    conn.close()
    return jsonify({"message": "Problem sucessfully added!"})

# Update an existing problem
@problem_blueprint.route("/<int:problem_id>", methods=["PUT"])
def update_problem(problem_id):
    data = request.get_json()
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE problems
        SET title = ?, difficulty = ?, topic = ?, status = ?, notes = ?, last_attempt = ?
        WHERE id = ?
    """, (
        data.get("title"),
        data.get("difficulty"),
        data.get("topic"),
        data.get("status"),
        data.get("notes"),
        data.get("last_attempt"),
        problem_id
    ))
    conn.commit()
    conn.close()
    return jsonify({"message": "Problem sucessfully updated!"})

# Delete an existing problem 
@problem_blueprint("/<int:problem_id>", methods=["DELETE"])
def delete_problem(problem_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM problems WHERE id = ?", (problem_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Problem sucessfullt deleted!"})