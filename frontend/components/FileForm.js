/*import './FileForm.css'
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
*/
import './FileForm.css';
import { useState } from 'react';

function FileForm() {
    const [file1, setFile1] = useState(null);
    const [file2, setFile2] = useState(null);

    const handleFileInputChange = (event, setFile) => {
        setFile(event.target.files[0]);
    }

    const handleSubmit = async (event, uploadEndpoint, file) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file_upload', file);

        try {
            const endpoint = `http://localhost:8000/${uploadEndpoint}/`; // Adjust the port if needed
            const response = await fetch(endpoint, {
                method: "POST",
                body: formData
            });

            if (response.ok) {
                console.log("File uploaded successfully");
            } else {
                console.error("Failed to upload file");
            }
        } catch (error) {
            console.error(error);
        }
    }

    const handleGrade = async () => {
        try {
            const endpoint = "http://localhost:8000/grade"; // Adjust the port if needed
            const response = await fetch(endpoint, {
                method: "POST"
            });

            if (response.ok) {
                console.log("Grading initiated successfully");
            } else {
                console.error("Failed to initiate grading");
            }
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <div>
            <h1>Upload files</h1>
            <form onSubmit={(event) => handleSubmit(event, "uploadfile_1", file1)}>
                <input type="file" onChange={(event) => handleFileInputChange(event, setFile1)} />
                <button className="upl" type="submit">Upload Student's Answer</button>
            </form>

            <form onSubmit={(event) => handleSubmit(event, "uploadfile_2", file2)}>
                <input type="file" onChange={(event) => handleFileInputChange(event, setFile2)} />
                <button className="upl" type="submit">Upload Solution Manual</button>
            </form>

            <button className="grade" onClick={handleGrade}>Grade</button>

            

            {file1 && <p>{file1.name}</p>}
            {file2 && <p>{file2.name}</p>}
        </div>
    );
}

export default FileForm;
