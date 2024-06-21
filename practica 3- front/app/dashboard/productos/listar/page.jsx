'use client'

import Link from "next/link";
import { useState, useEffect } from "react";
import { useRouter } from 'next/navigation';
import Image from 'next/image';
import { listPCAducado, uploadImagen, saveProducto } from "@/app/hooks/Service_producto";

export default function ListaProductos() {
    const [persons, setPersons] = useState([]);
    const [message, setMessage] = useState('');

    useEffect(() => {
        const fetchProductos = async () => {
            try {
                const result = await listPCAducado();
                console.log('Datos recibidos:', result);
                if (result.data) {
                    setPersons(result.data);
                } else {
                    console.warn('No se encontraron datos en el resultado de la API');
                }
            } catch (error) {
                console.error('Error al obtener los datos:', error);
            }
        };
        fetchProductos();
    }, []);

    const handleBaja = (id) => {
        console.log(`Bajar cuenta con id: ${id}`);
    };

    const handleImagenChange = async (e, index) => {
        const file = e.target.files[0];

        try {
            const formData = new FormData();
            formData.append('imagen', file);
            const uploadResponse = await uploadImagen(formData);

            if (uploadResponse && uploadResponse.success) {
                console.log(`Imagen subida con éxito: ${uploadResponse.url}`);

                // Actualizar persons con la nueva imagen_url
                const updatedPersons = [...persons];
                updatedPersons[index].imagen_url = uploadResponse.url;
                setPersons(updatedPersons);

                // Guardar producto con la nueva imagen_url en la base de datos
                const productoData = {
                    ...updatedPersons[index],
                    imagen_url: uploadResponse.url
                };

                const response = await saveProducto(productoData);

                if (response && response.code === 200) {
                    console.log('Producto actualizado en la base de datos:', response.data);
                } else {
                    throw new Error('Error al guardar el producto en la base de datos');
                }

            } else {
                throw new Error('Error al subir la imagen');
            }
        } catch (error) {
            console.error('Error al subir la imagen:', error);
            setMessage('Error al subir la imagen');
        }
    };

    return (
        <>
            <main className="container text-center mt-5">
                <div className="container-fluid">
                    <h1 className="mb-4" style={{ fontSize: '3rem' }}>Lista de Productos Caducados</h1>

                    <table className="table table-bordered" style={{ borderColor: "ActiveBorder", fontSize: '25px' }}>
                        <thead className="table-active">
                            <tr>
                                <th>id</th>
                                <th>Nombre</th>
                                <th>Fecha_Fab</th>
                                <th>Fecha_ven</th>
                                <th>Cantidad</th>
                                <th>Estado</th>
                                <th>Descripción</th>
                                <th>Imagen</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            {persons.length === 0 ? (
                                <tr>
                                    <td colSpan="9">No hay datos disponibles</td>
                                </tr>
                            ) : (
                                persons.map((dato, index) => {
                                    console.log(`Datos del producto en la fila ${index + 1}:`, dato);
                                    return (
                                        <tr key={dato.external_id}>
                                            <th scope="row">{index + 0}</th>
                                            <td>{dato.nombre}</td>
                                            <td>{dato.fecha_fab}</td>
                                            <td>{dato.fecha_ven}</td>
                                            <td>{dato.cantidad}</td>
                                            <td>{dato.estado}</td>
                                            <td>{dato.descripcion}</td>
                                            <td>
                                                {dato.imagen_url && (
                                                    <img src={dato.imagen_url} alt={`Imagen de ${dato.nombre}`} style={{ maxWidth: '200px', maxHeight: '150px' }} />
                                                )}
                                                {index === 0 && (
                                                    <Image src="/images/Maiz.jpeg" alt="Descripción de la imagen" width={500} height={300} />

                                                )}

                                                {dato.imagen_url && (
                                                    <img src={dato.imagen_url} alt={`Imagen de ${dato.nombre}`} style={{ maxWidth: '200px', maxHeight: '150px' }} />
                                                )}
                                                {index === 1 && (
                                                    <Image src="/images/arroz.jpeg" alt="Descripción de la imagen" width={500} height={300} />

                                                )}

                                                <div className="mt-2">
                                                    <label htmlFor={`uploadImage${index}`} className="btn btn-primary" style={{ fontSize: '16px', marginBottom: 0 }}>
                                                        Subir Imagen
                                                    </label>
                                                    <input
                                                        type="file"
                                                        id={`uploadImage${index}`}
                                                        style={{ display: 'none' }}
                                                        onChange={(e) => handleImagenChange(e, index)}
                                                    />
                                                </div>
                                            </td>
                                            <td style={{ width: '280px' }}>
                                                <Link
                                                    href={`/person/${dato.external_id}`}
                                                    className="btn btn-warning font-weight-bold"
                                                    style={{ marginRight: "15px", fontSize: '20px' }}
                                                >
                                                    Modificar
                                                </Link>

                                                <div className="modal fade" id={`exampleModal${index}`} tabIndex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                                    <div className="modal-dialog">
                                                        <div className="modal-content">
                                                            <div className="modal-header">
                                                                <h5 className="modal-title" id="exampleModalLabel">Confirmación</h5>
                                                                <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                                            </div>
                                                            <div className="modal-body">
                                                                ¿Estás seguro que quieres bajar esta cuenta?
                                                            </div>
                                                            <div className="modal-footer">
                                                                <button type="button" className="btn btn-secondary" data-bs-dismiss="modal" style={{ fontSize: '20px' }}>Cancelar</button>
                                                                <button type="button" className="btn btn-primary" data-bs-dismiss="modal" style={{ fontSize: '20px' }} onClick={() => handleBaja(dato.external_id)}>Confirmar</button>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </td>
                                        </tr>
                                    );
                                })
                            )}
                        </tbody>
                    </table>
                </div>
            </main>
        </>
    );
}
