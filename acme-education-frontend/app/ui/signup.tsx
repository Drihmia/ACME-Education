// "use client";

// import useSWR, { mutate } from "swr";
// import { FieldSet, MyTextAndSelectInput, MyTextInput } from "./form";
// import { Formik, Form } from "formik";
// import { signupSchema, updateSchema } from "../validation/schema";
// import { useEffect, useState } from "react";
// import { SignUpModal } from "./signupModal";
// import { fetcher } from "../lib/fetch";
// import { cityProps, institutionProps } from "../types";
// import { Icon } from "@iconify/react/dist/iconify.js";

// interface signupProps {
//   first_name: string;
//   last_name: string;
//   email: string;
//   phone_number: string;
//   password: string;
//   confirm_password: string;
//   isTeacher: string;
//   city: string;
//   city_id?: string;
//   institution: string;
//   institution_id?: string;
//   subjects_id?: string[];
// }

// interface responseProps {
//   status: string;
//   message: string;
// }

// interface selectedCityProps {
//   status: boolean;
//   id: string;
// }

// export const SignUpForm = ({
//   action,
//   profile,
//   close,
// }: {
//   action: string;
//   profile?: any;
//   close?: () => void;
// }) => {
//   const [response, setResponse] = useState<responseProps>({
//     status: "",
//     message: "",
//   });
//   const [isModal, setModal] = useState(false);
//   const closeModal = () => setModal(false);

//   const [institutionsData, setInstitutionsData] = useState<institutionProps[]>(
//     []
//   );

//   const [selectedCity, setCity] = useState<selectedCityProps>({
//     status: false,
//     id: "",
//   });

//   useEffect(() => {
//     if (selectedCity.id != "") {
//       fetch(
//         `http://127.0.0.1:5000/api/v1/cities/${selectedCity.id}/institutions`
//       )
//         .then((res) => res.json())
//         .then((data) => setInstitutionsData(data));
//     } else {
//       setInstitutionsData([]);
//     }
//   }, [selectedCity]);

//   const checkValue = (status: boolean, id?: string) => {
//     if (status) {
//       setCity({ status: true, id: id! });
//     } else {
//       setCity({ status: false, id: "" });
//     }
//   };

//   const { data: citiesData } = useSWR(
//     "http://127.0.0.1:5000/api/v1/cities",
//     fetcher
//   );

//   // clearCache()
//   const subjectsUrl = "http://127.0.0.1:5000/api/v1/subjects";
//   const profileUrl = `http://127.0.0.1:5000/api/v1/teachers/${profile.id}`;

//   const { data: subjectsList } = useSWR(subjectsUrl, fetcher);

//   mutate(subjectsUrl);

//   const submitForm = async (values: signupProps) => {
//     const city = citiesData?.find(
//       (item: cityProps) => item.name == values.city
//     );
//     if (city) values.city_id = city.id;

//     const institution = institutionsData?.find(
//       (item: institutionProps) => item.name == values.institution
//     );
//     if (institution) values.institution_id = institution.id;

//     console.log(values);

//     try {
//       const response = await fetch(
//         `http://127.0.0.1:5000/api/v1/${
//           values.isTeacher == "true" ? "teachers" : "students"
//         }/${action == "update" ? profile.id : ""}`,
//         {
//           method: action == "signup" ? "POST" : "PUT",
//           body: JSON.stringify(values),
//           headers: {
//             "Content-Type": "application/json",
//           },
//         }
//       );

//       const res_data = await response.json();

//       if (res_data["error"]) {
//         setResponse({ status: "error", message: res_data["error"] });
//         alert(res_data["error"]);
//       } else {
//         setResponse({ status: "success", message: "OK" });
//         if (action == "update") {
//           alert("Profile updated");
//           if (close) {
//             close();
//           }
//           mutate(profileUrl);
//         }
//       }
//     } catch (e) {
//       let errorMessage = "Something went wrong. Try again later.";
//       if (e instanceof Error) {
//         errorMessage = e.message;
//       }
//       setResponse({ status: "error", message: errorMessage });
//     } finally {
//       setModal(true);
//     }
//   };

//   return (
//     <>
//       <div
//         className={`w-full ${
//           action === "signup" ? "max-w-xl shadow-xl" : ""
//         } flex flex-col items-center justify-center gap-4 py-8 bg-white rounded-2xl`}
//       >
//         <div className="w-full text-center">
//           {action === "signup" ? (
//             <>
//               <h2 className="font-semibold text-3xl md:text-4xl capitalize mb-2 md:mb-4">
//                 Sign Up
//               </h2>
//               <p className="max-w-sm mx-auto">
//                 Join millions of institutions, teachers and students using ACME
//                 Education
//               </p>
//             </>
//           ) : (
//             <h2 className="font-semibold text-3xl md:text-4xl capitalize mb-2 md:mb-4">
//               Update profile
//             </h2>
//           )}
//         </div>
//         <Formik
//           initialValues={{
//             first_name: action == "update" ? profile.first_name : "",
//             last_name: action == "update" ? profile.last_name : "",
//             email: action == "update" ? profile.email : "",
//             phone_number:
//               action == "update"
//                 ? profile.phone_number
//                 : "",
//             password: "",
//             confirm_password: "",
//             institution: action == "update" ? profile.institution : "",
//             city: action == "update" ? profile.city : "",
//             isTeacher:
//               action == "update"
//                 ? profile.__class__ == "Teacher"
//                   ? "true"
//                   : "false"
//                 : "",
//           }}
//           validationSchema={action === "update" ? updateSchema : signupSchema}
//           onSubmit={(values, { setSubmitting }) => {
//             submitForm(values);
//             setSubmitting(false);
//           }}
//         >
//           <Form className="w-full flex flex-col md:grid md:grid-cols-2 lg:gap-4 items-center p-4 md:p-8 lg:px-16">
//             <MyTextInput
//               label="Email Address"
//               name="email"
//               type="email"
//               placeholder="you@example.com"
//             />
//             <MyTextInput
//               label="First Name"
//               name="first_name"
//               type="text"
//               placeholder="John"
//             />
//             <MyTextInput
//               label="Last Name"
//               name="last_name"
//               type="text"
//               placeholder="Doe"
//             />
//             <MyTextInput
//               label="Phone Number"
//               name="phone_number"
//               type="number"
//               placeholder="+2334045002001"
//             />
//             {action === "signup" && (
//               <>
//                 <MyTextInput
//                   label="Password"
//                   name="password"
//                   type="password"
//                   placeholder=""
//                 />
//                 <MyTextInput
//                   label="Confirm Password"
//                   name="confirm_password"
//                   type="password"
//                   placeholder=""
//                 />
//               </>
//             )}
//             <MyTextAndSelectInput
//               label="City"
//               name="city"
//               data={citiesData}
//               checkValue={checkValue}
//               type="text"
//               placeholder="e.g MarsCity"
//               disabled={profile ? true : false}
//             />
//             <MyTextAndSelectInput
//               label="Name of Institution"
//               name="institution"
//               data={institutionsData}
//               type="text"
//               disabled={!selectedCity.status}
//               placeholder="e.g Insitute of Science and Technology"
//             />
//             {action === "signup" && (
//               <FieldSet
//                 label="Are you a Teacher or a Student?"
//                 name="isTeacher"
//                 options={[
//                   {
//                     name: "isTeacher",
//                     label: "Teacher",
//                     value: true,
//                     type: "radio",
//                   },
//                   {
//                     name: "isTeacher",
//                     label: "Student",
//                     value: false,
//                     type: "radio",
//                   },
//                 ]}
//               />
//             )}
//             {action === "update" && subjectsList && (
//               <FieldSet
//                 label="Subjects"
//                 name="subjects_id"
//                 options={subjectsList.map((sub: any) => {
//                   const newSub = { ...sub };
//                   newSub.label = sub.name;
//                   newSub.name = "subjects_id";
//                   newSub.value = sub.id;
//                   newSub.type = "checkbox";
//                   return newSub;
//                 })}
//               />
//             )}
//             <div className="flex items-center gap-4 justify-center md:col-span-full">
//               <button
//                 type="submit"
//                 className="w-40 py-2 mt-8 bg-blue-100 text-black hover:text-white hover:bg-blue-700 capitalize rounded-xl"
//               >
//                 {action === "signup" ? "sign up" : "update"}
//               </button>
//               {action === "update" && (
//                 <div
//                   onClick={() => {
//                     if (
//                       confirm("Are you sure you want to go cancel?") &&
//                       close
//                     ) {
//                       close();
//                     }
//                   }}
//                   className="w-40 mt-8 flex items-center gap-1 justify-center p-2 bg-slate-200 hover:bg-black rounded-xl hover:text-white cursor-pointer"
//                 >
//                   <Icon icon="pajamas:cancel" /> Cancel
//                 </div>
//               )}
//             </div>
//           </Form>
//         </Formik>
//       </div>
//       {isModal && action === "signup" && (
//         <SignUpModal closeModal={closeModal} response={response} />
//       )}
//     </>
//   );
// };
