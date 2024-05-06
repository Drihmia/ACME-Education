import * as yup from "yup";

const emailRegex = /[a-z0-9]+@[a-z]+.[a-z]{2,3}/;
const phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
const passwordRegex =
  /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/;

const allowedDomains = [
  "gmail.com",
  "yahoo.com",
  "outlook.com",
  "aol.com",
  "icloud.com",
  "protonmail.com",
  "yandex.com",
  "zoho.com",
];

const validateEmailDomain = (value?: string) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (value) {
    if (!regex.test(value)) {
      return false; // Invalid email format
    }

    const domain = value.split("@")[1];
    return allowedDomains.includes(domain);
  }
};

export const signupTeacherSchema = yup.object().shape({
  first_name: yup.string().required("First Name is required"),
  last_name: yup.string().required("Last Name is required"),
  email: yup
    .string()
    .email()
    .matches(emailRegex, "Email is invalid.")
    .test("is-valid-domain", "Invalid email address", validateEmailDomain)
    .required("Email address is required"),
  phone_number: yup
    .string()
    .matches(phoneRegex, "Invalid phone number")
    .required("Phone number is required"),
  password: yup
    .string()
    .matches(
      passwordRegex,
      "Password must be at least 8 characters and have at least one uppercase, one lowercase, a number and a special characters"
    )
    .required("Password is required"),
  confirm_password: yup
    .string()
    .oneOf([yup.ref("password")], "Mismatched passwords")
    .required("Please confirm your password"),
  institution: yup.string().required("Name of institution is required"),
  city: yup.string().required("Name of city is required"),
  subjects: yup.array().of(yup.string()),
  gender: yup.string().oneOf(["F", "M"], "Gender is required").required()
});

export const signupStudentSchema = yup.object().shape({
  first_name: yup.string().required("First Name is required"),
  last_name: yup.string().required("Last Name is required"),
  email: yup
    .string()
    .email()
    .matches(emailRegex, "Email is invalid.")
    .test("is-valid-domain", "Invalid email address", validateEmailDomain)
    .required("Email address is required"),
  phone_number: yup
    .string()
    .matches(phoneRegex, "Invalid phone number")
    .required("Phone number is required"),
  password: yup
    .string()
    .matches(
      passwordRegex,
      "Password must be at least 8 characters and have at least one uppercase, one lowercase, a number and a special characters"
    )
    .required("Password is required"),
  confirm_password: yup
    .string()
    .oneOf([yup.ref("password")], "Mismatched passwords")
    .required("Please confirm your password"),
  institution: yup.string().required("Name of institution is required"),
  city: yup.string().required("Name of city is required"),
  teacher_email: yup.string(),
  class_id: yup.string().required("Class id is required"),
  gender: yup.string().oneOf(["F", "M"], "Gender is required").required()
});

export const updateTeacherSchema = yup.object().shape({
  first_name: yup.string().required("First Name is required"),
  last_name: yup.string().required("Last Name is required"),
  email: yup
    .string()
    .email()
    .matches(emailRegex, "Email is invalid.")
    .test("is-valid-domain", "Invalid email address", validateEmailDomain)
    .required("Email address is required"),
  phone_number: yup
    .string()
    .matches(phoneRegex, "Invalid phone number")
    .required("Phone number is required"),
  institution: yup.string().required("Name of institution is required"),
  city: yup.string().required("Name of city is required"),
  subjects: yup.array().of(yup.string()),
});

export const updateStudentSchema = yup.object().shape({
  first_name: yup.string().required("First Name is required"),
  last_name: yup.string().required("Last Name is required"),
  email: yup
    .string()
    .email()
    .matches(emailRegex, "Email is invalid.")
    .test("is-valid-domain", "Invalid email address", validateEmailDomain)
    .required("Email address is required"),
  phone_number: yup
    .string()
    .matches(phoneRegex, "Invalid phone number")
    .required("Phone number is required"),
  institution: yup.string().required("Name of institution is required"),
  city: yup.string().required("Name of city is required"),
  teacher_email: yup.string().email(),
  class_id: yup.string().required("Class id is required"),
  gender: yup.string().oneOf(["F", "M"], "Gender is required").required()
});

export const updatePasswordSchema = yup.object().shape({
  password: yup
    .string()
    .matches(
      passwordRegex,
      "Password must be at least 8 characters and have at least one uppercase, one lowercase, a number and a special characters"
    )
    .required("Password is required"),
  confirm_password: yup
    .string()
    .oneOf([yup.ref("password")], "Mismatched passwords")
    .required("Please confirm your password"),
});

export const forgotPasswordSchema = yup.object().shape({
  email: yup
    .string()
    .email()
    .test("is-valid-domain", "Invalid email address", validateEmailDomain)
    .required("Email address is required"),
});

export const signinSchema = yup.object().shape({
  email: yup
    .string()
    .email()
    .test("is-valid-domain", "Invalid email address", validateEmailDomain)
    .required("Email address is required"),
  password: yup.string().required(),
  isTeacher: yup
    .string()
    .oneOf(["true", "false"], "Terms must be accepted")
    .required(),
});

export const signupQuestion = yup.object().shape({
  answer: yup.string().oneOf(["true", "false"], "Must be a teacher or student").required()
})