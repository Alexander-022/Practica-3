'use client';

import { useState } from "react";
import { saveCensu, savePerson } from "@/app/hooks/Service_censu"; // Importa la función savePerson del módulo Service_person
import Link from "next/link";

import { useRouter } from 'next/navigation';
import { POST } from "@/app/hooks/Connection";
import swal from 'sweetalert';

export default function Censo() {
    const [startdate, setStartdate] = useState('');
    const [enddate, setEndate] = useState('');
    const [motive, setMotive] = useState('');
    
    const [message, setMessage] = useState('');


    const handleRegister = async () => {

        if (!startdate || !enddate || !motive ) {
            setMessage('Error: Todos los campos son obligatorios');
            return;
        }

        const data = {
            startdate: startdate,
            enddate: enddate,
            motive: motive,
            
        };

        try {
            await saveCensu(data);
            swal({
                title: "SUCCESS",
                text: "Los datos se han guardado correctamente.",
                icon: "success",
                button: "Aceptar",
                timer: 4000,
                closeOnEsc: true
            });
            // Limpiar los campos después de guardar los datos
            setStartdate('');
            setEndate('');
            setMotive('');
            
        } catch (error) {
            console.error('Error al enviar los datos del censo:', error);
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

    const currentDate = new Date().toISOString().split('T')[0];

    return (
        <section className="vh-100 bg-image" style={{ backgroundImage: "url('https://mdbcdn.b-cdn.net/img/Photos/new-templates/search-box/img4.webp')" }}>
            <div className="mask d-flex align-items-center h-100 gradient-custom-3">
                <div className="container h-100">
                    <div className="row d-flex justify-content-center align-items-center h-100">
                        <div className="col-12 col-md-9 col-lg-7 col-xl-6">
                            <div className="card" style={{ borderRadius: "15px" }}>
                                <div className="card-body p-5">
                                    <h2 className="text-uppercase text-center mb-5"><strong>Registrar Censo</strong></h2>
                                    {/* Agregar mensaje de alerta */}
                                    {message && (
                                        <div className={`alert alert-${message.includes('Error') ? 'danger' : 'success'}`} role="alert">
                                            {message}
                                        </div>
                                    )}
                                    <form>
                                        

                                        <div>
                                            

                                            <div className="form-outline mb-4">
                                                <input
                                                    type="date"
                                                    value={startdate}
                                                    // Establecer la fecha máxima permitida
                                                    onChange={(e) => setStartdate(e.target.value)}
                                                    className="form-control form-control-lg"
                                                />
                                                <label className="form-label"><strong>Fecha de Inicio</strong></label>
                                            </div>
                                        </div>


                                        <div>


                                            <div className="form-outline mb-4">
                                                <input
                                                    type="date"
                                                    value={enddate}
                                                    
                                                    onChange={(e) => setEndate(e.target.value)}
                                                    className="form-control form-control-lg"
                                                />
                                                <label className="form-label"><strong>Fecha de Fin</strong></label>
                                            </div>
                                        </div>

                                        <div className="form-outline mb-4">
                                            <input type="text" value={motive} onChange={(e) => setMotive(e.target.value)} className="form-control form-control-lg" placeholder="Ingrese el motivo del censo" />
                                            <label className="form-label"><strong>Motivo</strong></label>
                                        </div>
                                        

                                        <div className="d-flex justify-content-center">
                                            <button type="button" onClick={handleRegister} className="btn btn-success btn-block btn-lg gradient-custom-4 text-body">Registrar</button>
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
