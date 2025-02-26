from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


if __name__ == "__main__":
    print("Hello Langchain..!!")

    # information = """
    #         Adolf Hitler[a] (20 April 1889 – 30 April 1945) was an Austrian-born German politician who was the dictator of Nazi Germany from 1933 until his suicide in 1945. He rose to power as the leader of the Nazi Party,[c] becoming the chancellor in 1933 and then taking the title of Führer und Reichskanzler in 1934.[d] His invasion of Poland on 1 September 1939 marked the start of the Second World War. He was closely involved in military operations throughout the war and was central to the perpetration of the Holocaust: the genocide of about six million Jews and millions of other victims.
    #         Hitler was born in Braunau am Inn in Austria-Hungary and moved to Germany in 1913. He was decorated during his service in the German Army in World War I, receiving the Iron Cross. In 1919, he joined the German Workers' Party (DAP), the precursor of the Nazi Party, and in 1921 was appointed leader of the Nazi Party. In 1923, he attempted to seize power in a failed coup in Munich and was sentenced to five years in prison, serving just over a year. While there, he dictated the first volume of his autobiography and political manifesto Mein Kampf (My Struggle). After his early release in 1924, Hitler gained popular support by attacking the Treaty of Versailles and promoting pan-Germanism, antisemitism, and anti-communism with charismatic oratory and Nazi propaganda. He frequently denounced communism as being part of an international Jewish conspiracy. By November 1932, the Nazi Party held the most seats in the Reichstag, but not a majority. Former chancellor Franz von Papen and other conservative leaders convinced President Paul von Hindenburg to appoint Hitler as chancellor on 30 January 1933. Shortly thereafter, the Reichstag passed the Enabling Act of 1933, which began the process of transforming the Weimar Republic into Nazi Germany, a one-party dictatorship based on the totalitarian and autocratic ideology of Nazism.
    #         Upon Hindenburg's death on 2 August 1934, Hitler became simultaneously the head of state and government, with absolute power. Domestically, Hitler implemented numerous racist policies and sought to deport or kill German Jews. His first six years in power resulted in rapid economic recovery from the Great Depression, the abrogation of restrictions imposed on Germany after World War I, and the annexation of territories inhabited by millions of ethnic Germans, which initially gave him significant popular support. One of Hitler's key goals was Lebensraum (lit. 'living space') for the German people in Eastern Europe, and his aggressive, expansionist foreign policy is considered the primary cause of World War II in Europe. He directed large-scale rearmament and, on 1 September 1939, invaded Poland, causing Britain and France to declare war on Germany. In June 1941, Hitler ordered an invasion of the Soviet Union. In December 1941, he declared war on the United States. By the end of 1941, German forces and the European Axis powers occupied most of Europe and North Africa. These gains were gradually reversed after 1941, and in 1945 the Allied armies defeated the German army. On 29 April 1945, he married his longtime partner, Eva Braun, in the Führerbunker in Berlin. The couple committed suicide the next day to avoid capture.
    #         The historian and biographer Ian Kershaw described Hitler as "the embodiment of modern political evil".[3] Under Hitler's leadership and racist ideology, the Nazi regime was responsible for the genocide of an estimated six million Jews and millions of other victims, whom he and his followers deemed Untermenschen (lit. 'subhumans') or socially undesirable. Hitler and the Nazi regime were also responsible for the deliberate killing of an estimated 19.3 million civilians and prisoners of war. In addition, 28.7 million soldiers and civilians died as a result of military action in the European theatre. The number of civilians killed during World War II was unprecedented in warfare, and the casualties constitute the deadliest conflict in history.
    #     """

    # summary_template = """
    #     given the information {information} about a person from I want you to create:
    #     1. a short summary
    #     2. two interesting facts about them
    # """

    information = "Pizza"
    summary_template = """
    Write a small and simple romantic poem
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    # llm = ChatOllama(model="llama3.2")
    llm = ChatOllama(model="mistral-nemo")

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(res)
