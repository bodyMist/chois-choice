import Part from "./Part";

export default function PartList(props) {
  const {list} = props;
  return (
    <div className="StuffList">
      {list.map((listdata) => {
        <Part 
         component_id={listdata.component_id}
         image_url={listdata.image_url}
         name={listdata.name}
        />
      })}
    </div>
  );
}