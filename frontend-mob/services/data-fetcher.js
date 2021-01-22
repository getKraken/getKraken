import jwt_decode from "jwt-decode";
import axios from 'axios';

export default async function fetchAccessToken() {

    let accessToken = localStorage.getItem('kraken-access-token');

    if (!tokenIsFresh(accessToken)) {
        accessToken = await refreshToken();
        localStorage.setItem('kraken-access-token', accessToken);
    }

    return accessToken;

}

function tokenIsFresh(accessToken) {

    let decodedToken = jwt_decode(accessToken);

    console.log("Decoded Token", decodedToken);
    let currentDate = new Date();

    // JWT exp is in seconds
    if (decodedToken.exp * 1000 < currentDate.getTime()) {
        console.log("Token expired.");
        return false;
    } else {
        return true;
    }
}
async function refreshToken() {

    let url = "https://get-kraken.herokuapp.com/api/v1/token/refresh/";

    const refresh = localStorage.getItem('kraken-refresh-token');

    const response = await axios.post(url, { refresh });

    let JWTToken = response.data.access;

    return JWTToken

}
export async function getSeriesData(id=null) {
    return await getResourceData("series", id);
}

export async function getEventData(id=null) {
    return await getResourceData('event', id);
}

export async function getGenerateData(id){
    const JWTToken = await fetchAccessToken();
    if(id != null){
        const url = `https://get-kraken.herokuapp.com/api/v1/series/${id}/generate-draft-order/`;

        console.log('resource url', url);
        let config = { headers: { "Authorization": `Bearer ${JWTToken}` } };
        try{
            let response = await axios.get(url, config);
            return response.data;
        }catch(e){
            console.error(e);
        }
    }
    

}
async function getResourceData(noun, id=null) {

    const JWTToken = await fetchAccessToken();

    let url = `https://get-kraken.herokuapp.com/api/v1/${noun}/`;

    if(id != null) {
        url += `${id}/`;
    }

    console.log('resource url', url);

    let config = { headers: { "Authorization": `Bearer ${JWTToken}` } };

    try {

        let response = await axios.get(url, config);

        return response.data;

    } catch (e) {

        console.error("Failed to fetch series data")
    }
}
