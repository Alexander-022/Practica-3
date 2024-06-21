import Cookies from 'js-cookie';
import {GET} from './Connection';
import {POST} from './Connection';

export async function listProducto (token) {
    let data = null
    try {
        data = await GET('producto', token);
    } catch (error) {
        return error.response.data;
    }
    return data.data;
}

export async function listPCAducado (token) {
    let data = null
    try {
        data = await GET('lproducto/caducado', token);
    } catch (error) {
        return error.response.data;
    }
    return data.data;
}

export async function lisstPAlCaducar (token) {
    let data = null
    try {
        data = await GET('lproducto/al/caducar', token);
    } catch (error) {
        return error.response.data;
    }
    return data.data;
}


export async function saveProducto (token) {
    let data = null
    try {
        data = await POST('loteproducto/save', token);
    } catch (error) {
        return error.response.data;
    }
    return data.data;
}

export async function uploadImagen (token) {
    let data = null
    try {
        data = await POST('update/image', token);
    } catch (error) {
        return error.response.data;
    }
    return data.data;
}