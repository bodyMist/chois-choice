
export default function Datail ({id, name}) {
  return (
    <>
      <input
                type="checkbox"
                id={id}
            />
            &nbsp;{name}&nbsp;
    </>
  );
}