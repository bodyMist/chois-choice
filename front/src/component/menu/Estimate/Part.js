export default function Part({component_id, image_url,  name}) {
 return(
  <>
      <div className="StuffIcon">
           <img alt="1" src={image_url}/>
      </div>
      <div className="btn text-left" id={component_id}>
           <span>CPU : </span>
           {/* <span className="label label-info">추천</span> */}
           <span>{name}</span>
      </div>
  </>
 );
}