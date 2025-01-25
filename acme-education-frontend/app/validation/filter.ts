import * as yup from "yup";

export const filterSchema = yup.object().shape({
    teacher: yup.string(),
    subject: yup.string(),
    name: yup.string(),
    public: yup.string(),
    class: yup.string(),
    institution: yup.string()
  });
  
