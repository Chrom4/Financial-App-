import styles from "./index.module.css"

const Container = ({ className, children }) => {

    const containerCn = [styles.Container, className].join(" ");

    return <div className={containerCn}>
        {children}
    </div>
}

export default Container;