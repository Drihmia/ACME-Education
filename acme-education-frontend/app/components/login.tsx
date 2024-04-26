// "use client";

// import React, { useState } from "react";
// import { emailRegex } from "../lib/regex";
// import googleImg from '@/app/assets/btn_google_signin_dark_pressed_web.png'
// import Image from "next/image";
// import ShowPassword from "./ShowPassword";
// import Link from "next/link";

// const Login = () => {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [error, setError] = useState({ email: "", password: "" });

//   const alertError = (type: string) => {
//     if (type === "email") {
//       setError({ ...error, email: "Please type in a valid email" });
//     } else {
//       setError({ ...error, password: "Email or password incorrect" });
//     }
//   };

//   const handleLogin = async (e: React.SyntheticEvent) => {
//     e.preventDefault();

//     //check if email is in the correct format
//     if (!emailRegex.test(email)) {
//       alertError("email");
//       return;
//     }

//   };

//   return (
//     <section className="w-full h-full sm:max-w-sm sm:h-[90%] max-h-[540px] flex flex-col p-4 md:p-4 sm: bg-slate-100 rounded-lg shadow">
//       <h2 className="w-full py-2 text-center uppercase font-bold text-3xl">login</h2>
//       <div className="w-full h-[1px] bg-slate-900/20"></div>
//       <div className="w-48 h-14 mx-auto my-2 relative py-4">
//         <Image className="cursor-pointer" src={googleImg} alt="google btn" fill sizes="" />
//       </div>
//       <div className="relative w-full">
//         <p className="relative w-8 h-8 mx-auto flex items-center justify-center text-slate-900/50 uppercase border border-slate-900/20 rounded-full z-[5] bg-slate-100">or</p>
//         <div className="absolute top-1/2 left-0 w-full h-[1px] bg-slate-900/20"></div>
//       </div>
//       <form className="w-full h-full flex flex-col justify-between py-4" noValidate onSubmit={handleLogin}>
//         <div className="w-full grid gap-4">
//         <div className="w-full flex flex-col gap-0.5">
//           <span className="w-full text-center text-sm">{error.password}</span>
//           <label className="text-lg font-bold" htmlFor="email">Email</label>
//           <input
//             id="email"
//             name="email"
//             className="w-full h-10 text-base p-2 rounded"
//             type="text"
//             placeholder="Your email"
//             value={email}
//             onChange={(e) => {
//               setEmail(e.target.value);
//               setError({ ...error, email: "" });
//             }}
//           />
//           <span className="w-full text-center text-[8px]">{error.email}</span>
//         </div>
//         <div className="w-full flex flex-col gap-0.5">
//           <label className="relative text-lg font-bold" htmlFor="password">Password
//           <input
//             id="password"
//             name="password"
//             className="w-full h-10 text-base p-2 rounded"
//             type="password"
//             placeholder="Password"
//             value={password}
//             onChange={(e) => {
//               setPassword(e.target.value);
//               setError({ ...error, password });
//             }}
//           />
//           <ShowPassword inputId={"password"} />
//           </label>
//         </div>
//         </div>
//         <article className="w-full flex flex-col justify-center items-end gap-2">
//           <button className="w-20 p-2 uppercase rounded-lg text-slate-50 hover:text-slate-900 bg-slate-900 hover:bg-slate-400" type="submit">
//             login
//           </button>
//           <p className="cursor-pointer hover:underline">Forgot Password?</p>
//           <Link href={`/signup`} className="hover:underline">Do not have an account? Click here to Sign Up</Link>
//         </article>
//       </form>
//     </section>
//   );
// };

// export default Login;