from flask import Blueprint, request, jsonify
from .assembler import Assembler
from .simulator import Simulator
from flask_cors import CORS

bp = Blueprint('routes', __name__)
CORS(bp)

assembler = Assembler()
simulator = Simulator()

@bp.route('/assemble', methods=['POST'])
def assemble():
    data = request.get_json()
    assembly_code = data.get('assembly_code')
    if not assembly_code:
        return jsonify({"error": "No assembly code provided"}), 400
    try:
        machine_code = assembler.assemble(assembly_code)
        return jsonify({"machine_code": machine_code}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route('/simulate', methods=['POST'])
def simulate():
    data = request.get_json()
    machine_code = data.get('machine_code')
    if not machine_code:
        return jsonify({"error": "No machine code provided"}), 400
    simulator.load_program(machine_code)
    simulator.run()
    return jsonify({
        "registers": simulator.registers,
        "memory": simulator.memory[:len(machine_code)]
    }), 200
