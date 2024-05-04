import * as yup from "yup";

export const lessonSchema = yup.object().shape({
    subject: yup.string().required("Subject required"),
    institution: yup.string().required("Institution ID required"),
    name: yup.string().required("Name of lesson required"),
    download_link: yup.string().required("Download link to lesson required"),
    description: yup.string().required("Description of lesson required"),
    public: yup.string().oneOf(["true", "false"], "This is required").required(),
  });
  