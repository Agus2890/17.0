# -*- coding: utf-8 -*-

import base64
from odoo import http, api
from odoo.http import Controller, Response, request, route
from odoo.exceptions import AccessError, MissingError, ValidationError
import json
#from odoo.addons.web.controllers.main import _serialize_exception
from odoo.addons.web.controllers.main import content_disposition
#_serialize_exception,
from datetime import datetime

import os
import shutil
import tempfile
class WebFilesCfdi(http.Controller):


    @http.route('/generate_zip', type='http', auth='user')
    def generate_zip(self,**kwargs):
        data_inv=kwargs.get('inv_ids')
        move_ids= request.env['account.move'].browse(json.loads(data_inv))
        data_files=[]
        for line in move_ids:
            data_attachment=[]
            attachment_ids=request.env['ir.attachment'].search([('res_model', '=', 'account.move'),('res_id', '=', line.id)])
            for att in attachment_ids:
                if att.datas:
                    file_data = base64.b64decode(att.datas)
                    safe_name = att.name.replace('/', '_').replace('\\', '_')  # Evitar nombres de archivo inválidos
                    data_attachment.append({'name': safe_name, 'data': file_data})
            data_files.append({
                'name':line.name.replace('/','').replace('-',''),
                'files_atts':data_attachment
                })
        date=datetime.now().strftime('%Y_%m_%d')
        temp_dir = '/tmp/odoo_zip_folder'
        zip_file_path = f'/tmp/odoo_invoice_{date}.zip'

        try:
            # Crear el directorio raíz si no existe
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)

            # Crear carpetas y archivos dentro de cada una
            for i in data_files:  # Cambia 5 por la cantidad deseada de carpetas/archivos
                file_name=i['name']
                subfolder_path = os.path.join(temp_dir, f'{file_name}')
                os.makedirs(subfolder_path, exist_ok=True)  # Crea la subcarpeta

                # Crear un archivo dentro de la subcarpeta
                for att in  i['files_atts']:
                    file_path = os.path.join(subfolder_path, att['name'])
                    with open(file_path, 'wb') as file:  # Abrir en modo binario
                        file.write(att['data'])
                    #with open(os.path.join(subfolder_path, att['name']), 'w') as file:
                    #    file.write(f'Contenido del archivo {file_name}\n')

            # Comprimir el directorio en un archivo ZIP
            shutil.make_archive(base_name=zip_file_path.replace('.zip', ''), format='zip', root_dir=temp_dir)

            # Leer el archivo ZIP y enviarlo como respuesta HTTP
            with open(zip_file_path, 'rb') as zip_file:
                response = request.make_response(
                    zip_file.read(),
                    headers=[
                        ('Content-Type', 'application/zip'),
                        ('Content-Disposition', f'attachment; filename=odoo_invoice_{date}.zip'),
                    ]
                )
            return response

        finally:
            # Limpiar los archivos temporales
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
            if os.path.exists(zip_file_path):
                os.remove(zip_file_path)
    