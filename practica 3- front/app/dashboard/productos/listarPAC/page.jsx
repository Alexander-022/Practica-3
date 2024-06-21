'use client'
import Link from "next/link";
import { useState, useEffect } from "react";
import { useRouter } from 'next/navigation';
import { GET } from "@/app/hooks/Connection";
import { lisstPAlCaducar, listPCAducado, listProducto } from "@/app/hooks/Service_producto";

export default function () {
    const [persons, setProductoCAlCaducar] = useState([]);

    useEffect(() => {
        const fetchProductoCAlCaducar = async () => {
            try {
                const result = await lisstPAlCaducar();
                console.log('Datos recibidos:', result);
                setProductoCAlCaducar(result.data || []);
            } catch (error) {
                console.error('Error al obtener los datos:', error);
            }
        };
        fetchProductoCAlCaducar();
    }, []);

    const handleBaja = (id) => {
        // Lógica para manejar la baja de la cuenta
        console.log(`Bajar cuenta con id: ${id}`);
    };

    return (
        <>
            <main className="container text-center mt-5">
                <div className="container-fluid">
                <h1 className="mb-4" style={{ fontSize: '3rem' }}>Lista de Productos al Caducar</h1>
                    <Link href="/censo">
                    </Link>
                    <table className="table table-bordered" style={{ borderColor: "ActiveBorder", fontSize: '25px' }}>
                        <thead className="table-active">
                            <tr>
                                <th>id</th>
                                <th>Nombre</th>
                                <th>Fecha_Fab</th>
                                <th>Fecha_ven</th>
                                <th>Cantidad</th>
                                <th>Estado</th>
                                <th>Descripcion</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            {persons.length === 0 ? (
                                <tr>
                                    <td colSpan="5">No hay datos disponibles</td>
                                </tr>
                            ) : (
                                persons.map((dato, index) => (
                                    <tr key={dato.external_id}>
                                        <th scope="row">{index + 1}</th>
                                        <td>{dato.nombre}</td>
                                        <td>{dato.fecha_fab}</td>
                                        <td>{dato.fecha_ven}</td>
                                        <td>{dato.cantidad}</td>
                                        <td>{dato.estado}</td>
                                        <td>{dato.descripcion}</td>
                                        <td style={{ width: '280px' }}>
                                            <Link
                                                style={{ marginRight: "15px", fontSize: '20px' }}
                                                href={`/person/${dato.external_id}`}
                                                className="btn btn-warning font-weight-bold"
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
                                ))
                            )}
                        </tbody>
                    </table>
                </div>
            </main>
        </>
    );
}
