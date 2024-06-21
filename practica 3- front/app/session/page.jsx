'use client'

import './login.css';

import * as Yup from 'yup';

import Cookies from 'js-cookie';
import { login } from '../hooks/Service_authenticate';
import swal from 'sweetalert';
import { useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { useRouter } from 'next/navigation';
import { yupResolver } from '@hookform/resolvers/yup';

export default function Session() {
  const router = useRouter();
  const validationSchema = Yup.object().shape({
    correo: Yup.string().trim().required('Ingrese su correo'),
    clave: Yup.string().trim().required('Ingrese clave')
  });

  const formOptions = { resolver: yupResolver(validationSchema) };
  const { register, handleSubmit, formState } = useForm(formOptions);
  let { errors } = formState;

  useEffect(() => {
    const token = Cookies.get('token');
    if (!token) {
      router.push('/session');
    } else {
      router.push('/dashboard');
    }
  }, []);

  const sendInfo = (data) => {
    login(data).then((info) => {
      if (info.code == '200') {
        Cookies.set('token', info.datos.token);
        Cookies.set('user', info.datos.user);
        swal({
          title: "SUCCESS",
          text: "Welcome " + info.datos.user,
          icon: "success",
          button: "Accept",
          timer: 4000,
          closeOnEsc: true
        });
        const token = Cookies.get('token');
        if (token) {
          router.replace('/dashboard'); // Cambiado a router.replace
        }
      } else {
        console.log("Info object:", info.data);
        swal({
          title: "ERROR",
          text: info.datos.error,
          icon: "error",
          button: "Accept",
          timer: 4000,
          closeOnEsc: true
        });
        console.log(info);
        console.log("NO");
      }
    });
  };

  return (
    <div className="container vh-100 d-flex justify-content-center align-items-center">
      <div className="col-md-5 mx-auto p-0">
        <div className="card">
          <div className="login-box">
            <div className="login-snip">
              <input id="tab-1" type="radio" name="tab" className="sign-in" defaultChecked />
              <label htmlFor="tab-1" className="tab">Inicio</label>
              <input id="tab-2" type="radio" name="tab" className="sign-up" />
              <label htmlFor="tab-2" className="tab">Registrarse</label>
              <div className="login-space">
                <form onSubmit={handleSubmit(sendInfo)}>
                  <div className="login">
                    <div className="group">
                      <label htmlFor="correo" className="label">Correo</label>
                      <input
                        id="correo"
                        type="text"
                        {...register('correo')}
                        className={`input ${errors.correo ? 'is-invalid' : ''}`}
                        placeholder="Ingrese su correo"
                      />
                      <div className="invalid-feedback">{errors.correo?.message}</div>
                    </div>
                    <div className="group">
                      <label htmlFor="clave" className="label">Contraseña</label>
                      <input
                        id="clave"
                        type="password"
                        {...register('clave')}
                        className={`input ${errors.clave ? 'is-invalid' : ''}`}
                        placeholder="Ingrese su contraseña"
                      />
                      <div className="invalid-feedback">{errors.clave?.message}</div>
                    </div>
                    <div className="group">
                      <input type="submit" className="button" value="Iniciar" />
                    </div>
                    <div className="hr"></div>
                    <div className="foot">
                      <a href="#">¿Olvidó su contraseña?</a>
                    </div>
                  </div>
                </form>
                <div className="sign-up-form">
                  <div className="group">
                    <label htmlFor="user" className="label">Nombre de Usuario</label>
                    <input id="user" type="text" className="input" placeholder="Cree su nombre de usuario" />
                  </div>
                  <div className="group">
                    <label htmlFor="pass" className="label">Contraseña</label>
                    <input id="pass" type="password" className="input" placeholder="Cree su contraseña" />
                  </div>
                  <div className="group">
                    <label htmlFor="pass-repeat" className="label">Repita Contraseña</label>
                    <input id="pass-repeat" type="password" className="input" placeholder="Repita su contraseña" />
                  </div>
                  <div className="group">
                    <label htmlFor="correo-signup" className="label">Correo Electrónico</label>
                    <input id="correo-signup" type="text" className="input" placeholder="Ingrese su correo electrónico" />
                  </div>
                  <div className="group">
                    <input type="submit" className="button" value="Registrarse" />
                  </div>
                  <div className="hr"></div>
                  <div className="foot">
                    <label htmlFor="tab-1">¿Ya eres miembro?</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
