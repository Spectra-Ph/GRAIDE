import './FileForm.css'
import { useState } from 'react';


function FileForm() {

    const [file, setFile] = useState(null);

    const handleFileInputChange = (event) =>{
        console.log(event.target)
        setFile(event.target.files[0])
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file_upload', file);

        try {
            const endpoint = "http://localhost:8000/uploadfile/"
            const response = await fetch(endpoint, {
                method: "POST",
                body: formData
            });

            if (response.ok) {
                console.log("File uploaded successfully")

            } else {
                console.error("Failed to upload file");
            }
        } catch (error) {
            console.error(error);
        }
    }


    return(
        <div>
            <h1>Upload file</h1>

          <form onSubmit={handleSubmit}>
                <input type = "file" onChange={handleFileInputChange}/>

                <button className = "upl" type = "submit" >Upload</button>
          </form>

          <form className = "soln" onSubmit={handleSubmit}>
                <input type = "file" onChange={handleFileInputChange}/>

                <button className = "upl" type = "submit" >Upload</button>
          </form>

          { file && <p>{file.name}</p>}
        </div>
    )
}

export default FileForm;
