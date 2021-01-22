import Head from 'next/head'
import styles from '../styles/Home.module.css'
import RegisterForm from '../Forms/RegisterForm'
import LoginForm from '../forms/LoginForm'

export default function Home() {
  return (
    <div>
      {/* <h1> Registration Form</h1>
     <RegisterForm/> */}
     <h1> Login Form</h1>
     <LoginForm/>
    </div>
  )
}
