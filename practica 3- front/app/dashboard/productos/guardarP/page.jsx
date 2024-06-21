'use client'
import { useState } from "react";
import swal from 'sweetalert';
import { saveProducto } from "@/app/hooks/Service_producto";
import { uploadImagen } from "@/app/hooks/Service_producto";


export default function GuardarPro() {
    const [nombre, setNombre] = useState('');
    const [fecha_fab, setFecha_fab] = useState('');
    const [fecha_ven, setFecha_ven] = useState('');
    const [cantidad, setCantidad] = useState('');
    const [estado, setEstado] = useState('');
    const [descripcion, setDescripcion] = useState('');
    const [message, setMessage] = useState('');

    const handleRegister = async () => {
        console.log('Handle register clicked');
        console.log('Current state:', { nombre, fecha_fab, fecha_ven, cantidad, estado, descripcion });
    
        if (!nombre || !fecha_fab || !fecha_ven || !cantidad || !estado || !descripcion) {
            setMessage('Error: Todos los campos son obligatorios');
            console.log('Validation error:', { nombre, fecha_fab, fecha_ven, cantidad, estado, descripcion });
            return;
        }
    
        try {
            const productoData = {
                nombre,
                fecha_fab,
                fecha_ven,
                cantidad,
                estado,
                descripcion,
                imagen_url: ''  
            };
            console.log('Producto Data enviado:', productoData);
    
            const response = await saveProducto(productoData);
            console.log('Server response:', response);
    
            if (response && response.code === 200) {
                swal({
                    title: "SUCCESS",
                    text: "Los datos se han guardado correctamente.",
                    icon: "success",
                    button: "Aceptar",
                    timer: 4000,
                    closeOnEsc: true
                });
                // Limpiar los campos después de guardar los datos
                setNombre('');
                setFecha_fab('');
                setFecha_ven('');
                setCantidad('');
                setEstado('');
                setDescripcion('');
            } else {
                setMessage('Error: Ha ocurrido un error al guardar los datos.');
            }
        } catch (error) {
            console.error('Error al enviar los datos del producto:', error);
            setMessage('Error: Ha ocurrido un error al guardar los datos.');
            swal({
                title: "ERROR",
                text: "Ha ocurrido un error al guardar los datos.",
                icon: "error",
                button: "Aceptar",
                timer: 4000,
                closeOnEsc: true
            });
        }
    };
    

    return (
        <section className="vh-100 bg-image" style={{ backgroundImage: "url('https://mdbcdn.b-cdn.net/img/Photos/new-templates/search-box/img4.webp')" }}>
            <div className="mask d-flex align-items-center h-100 gradient-custom-3">
                <div className="container h-100">
                    <div className="row d-flex justify-content-center align-items-center h-100">
                        <div className="col-12 col-md-9 col-lg-7 col-xl-6">
                            <div className="card" style={{ borderRadius: "15px" }}>
                                <div className="card-body p-5">
                                    <h2 className="text-uppercase text-center mb-5"><strong>Registrar Productos</strong></h2>
                                    {message && (
                                        <div className="alert alert-danger" role="alert">
                                            {message}
                                        </div>
                                    )}
                                    <form>
                                        <div className="form-outline mb-4">
                                            <input
                                                type="text"
                                                value={nombre}
                                                onChange={(e) => setNombre(e.target.value)}
                                                className="form-control form-control-lg"
                                                placeholder="Ingrese el nombre del producto"
                                            />
                                            <label className="form-label"><strong>Nombres</strong></label>
                                        </div>

                                        <div className="form-outline mb-4">
                                            <input
                                                type="date"
                                                value={fecha_fab}
                                                onChange={(e) => setFecha_fab(e.target.value)}
                                                className="form-control form-control-lg"
                                            />
                                            <label className="form-label"><strong>Fecha de Fabricacion</strong></label>
                                        </div>

                                        <div className="form-outline mb-4">
                                            <input
                                                type="date"
                                                value={fecha_ven}
                                                onChange={(e) => setFecha_ven(e.target.value)}
                                                className="form-control form-control-lg"
                                            />
                                            <label className="form-label"><strong>Fecha de vencicimiento</strong></label>
                                        </div>

                                        <div className="form-outline mb-4">
                                            <input
                                                type="text"
                                                value={cantidad}
                                                onChange={(e) => setCantidad(e.target.value)}
                                                className="form-control form-control-lg"
                                                placeholder="Ingrese la cantidad"
                                            />
                                            <label className="form-label"><strong>Cantidad</strong></label>
                                        </div>

                                        <div className="form-outline mb-4">
                                            <select
                                                value={estado}
                                                onChange={(e) => setEstado(e.target.value)}
                                                className="form-select form-select-lg"
                                            >
                                                <option value="">Selecciona un estado</option>
                                                <option value="Bueno">Bueno</option>
                                                <option value="Al_caducar">Al caducar</option>
                                                <option value="Caducado">Caducado</option>
                                                <option value="No_disponible">No disponible</option>
                                            </select>
                                            <label className="form-label"><strong>Estado</strong></label>
                                        </div>

                                        <div className="form-outline mb-4">
                                            <input
                                                type="text"
                                                value={descripcion}
                                                onChange={(e) => setDescripcion(e.target.value)}
                                                className="form-control form-control-lg"
                                                placeholder="Ingrese la descripcion"
                                            />
                                            <label className="form-label"><strong>Descripcion</strong></label>
                                        </div>

                                        <div className="d-flex justify-content-center">
                                            <button
                                                type="button"
                                                onClick={handleRegister}
                                                className="btn btn-success btn-block btn-lg gradient-custom-4 text-body"
                                            >
                                                Registrar
                                            </button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}