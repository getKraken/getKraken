import React from 'react';
import {useRouter} from 'next/router';
import axios from 'axios';

export default function Id(){
  const router = useRouter()
  const {id} = router.query;
  return <div>Hello {id}</div>
}