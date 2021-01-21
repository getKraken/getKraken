import Head from 'next/head'
import styles from '../styles/Home.module.css'
import LonginForm from '../forms/LoginForm'
export default function Home() {
  return (
    <div >
      <h1>Home</h1>
      <LonginForm />
    </div>
  )
}
